from contextlib import redirect_stderr
import os
import unittest
import sqlite3
from pathlib import Path
from prettytable import PrettyTable
from models import MusicianRow, InstrumentNameRow, NumberofTrianglesRow, InstrumentRow
from dataclasses import astuple

#################################
# DON'T TOUCH THIS CODE. DON'T! #
#################################

class TestSqlQueries(unittest.TestCase):
    """ Class for grading SQL queries included in challenges directory
        Can be run with unittest or as __main__ to test without python errors."""

    @classmethod
    def setUpClass(cls):
        """Sets up an in-memory database fixture with a create script to be shared
           shared with all the tests
        """
        in_mem_db = sqlite3.connect(':memory:')
        # make each row searchable by column name
        in_mem_db.row_factory = TestSqlQueries.dict_factory
        in_mem_db.executescript(Path('musician.db.sql').read_text())
        cls._connection = in_mem_db

    @classmethod
    def tearDownClass(cls):
        """Close the db connection fixture before exiting
        """
        cls._connection.close()

    @staticmethod
    def dict_factory(cursor, row):
        """set the in-memory db's row_factory function to this method
           to allow each result row to be searched by column name 

        Args:
            cursor (Cursor): the connection cursor that has the column names
            row (Row): the current row the cursor is reading

        Returns:
            dict: the row represented as a dict 
        """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    
    @staticmethod
    def remove_duplicate_rows():
        pass

    def pretty_table(self, results, columns):
        """create a Pretty Table to display results

        Args:
            results (list[Any]): Will be a list of dataclass instances
            columns (list[str]): the column names to add as headers

        Returns:
            PrettyTable: the pretty table instance with the results and columns
        """
        pt = PrettyTable()
        pt.field_names = columns
        pt.add_rows(results)
        return pt

    def print_title(self, title):
        """Convenience method to pretty-print the title of each query result

        Args:
            title (str): whatever title you want to add to the printed result
        """
        print()
        print('-'*len(title))
        print(title)
        print('-'*len(title))

    def run_query(self, filepath):
        """Reads the SQL query file, executes the query, and catches any
           SQL errors

        Args:
            filepath (str): relative path to the query file

        Returns:
            Cursor: a db cursor to iterate over the results
        """
        txt = Path(filepath).read_text()
        cur = self._connection.cursor()
        results = None
        try:
            results = cur.execute(txt)
        except Exception as ex:
            print('Query caused following error -', ex)
            # still raise so the test gets graded
            raise
        return results
    
    def compare_results(self, results, raw_results, raw_columns, expected_columns, expected):
        """Assuming no SQL or missing columns, this method compares the expected
           rows to the actual rows returned from the db, and prints the results
           before raising (in the event of a validation error)

        Args:
            results (list[Any]): a list of rows converted to Python objects
            raw_results (list[dict]): the raw results to make sure all the user's column's are printed
            raw_columns (list[str]): a list of the columns from the query in the event that the python class properties
            don't match the actual results
            columns (list[str]): The column names (taken from the dataclass field names)
            expected (list[Any]): should be the same type as deserialized results, to compare
        """
        try:
            self.assertEqual(results, expected)
            print('Correct!')
        except AssertionError:
            print('Query is not quite right!')
            print()
            print('Your Results:')
            print(self.pretty_table([tuple(x.values()) for x in raw_results], raw_columns))
            print()
            print('Expected Results:')
            print(self.pretty_table([astuple(result) for result in expected], expected_columns))
            # still raise so the test can get graded 
            raise  
    
    def run_query_test(self, title, filepath, expected):
        """This is the method that will start each challenge

        Args:
            title (str): The header that will be printed with the results of a challenge
            filepath (str): the relative path to the sql query file
            expected (list[Any]): a list of Python objects of a type that can hold the row data
        """
        # infer the python dataclass to convert to from the first row of expected results
        row_type = type(expected[0])
        expected_columns = row_type.__dataclass_fields__

        self.print_title(title)

        # also get raw data to print user's results in case it doesn't pass
        cursor = self.run_query(filepath)
        raw_results = cursor.fetchall()
        if (len(raw_results)):
            raw_columns = raw_results[0].keys()
        else:
            if cursor.description is not None:
                raw_columns = set([x[0] for x in cursor.description])
            else:
                raw_columns = []
        
        try:
            # this will also validate that all columns needed are present
            results = self.run_query(filepath)
            results = [row_type(**{prop: row[prop] for prop in expected_columns}) for row in results]
        except KeyError as ex:
            print(f'Query was missing the following column: {ex}')
            # make sure there is something to pass to compare even if we know it will fail
            results = raw_results
        
        self.compare_results(results, raw_results, raw_columns, expected_columns, expected)
        
    def test_all(self):
        """We run all of the tests in one test method so that the program will stop
           executing as soon as one of the challenges is incorrect, to reduce the 
           amount of noise printed to the terminal every time the tests are run
        """
        self.run_query_test(
            title='#1: Get all musicians', 
            filepath='challenges/01select_star.sql',
            expected=[
                MusicianRow(MusicianId=1, MusicianName='Sun Ra'),
                MusicianRow(MusicianId=2, MusicianName='Weird Guy Down the Street'),
                MusicianRow(MusicianId=3, MusicianName='Julie')
            ])
        self.run_query_test(
            title = '#2: Get the Names of the Instruments played by "Julie"',
            filepath='challenges/02julies_instruments.sql',
            expected=[
                InstrumentNameRow(InstrumentName='Triangle'), 
                InstrumentNameRow(InstrumentName='Upright Bass')
                ])
        self.run_query_test(
            title='#3: Get the number of people that play Triangle',
            filepath='challenges/03num_trianglers.sql',
            expected=[NumberofTrianglesRow(NumberofTrianglers=2)])
        self.run_query_test(
            title='#4 Get the musician with the id of 2',
            filepath='challenges/04musician_number_2.sql',
            expected=[MusicianRow(MusicianId=2, MusicianName='Weird Guy Down the Street')]
        )
        self.run_query_test(
            title='#5 Get Instruments in alphabetical order',
            filepath='challenges/05instruments_in_order.sql',
            expected=[
                InstrumentRow(InstrumentId=5, InstrumentName='Fiddle', DifficultyId=2),
                InstrumentRow(InstrumentId=1, InstrumentName='Recorder', DifficultyId=1),
                InstrumentRow(InstrumentId=2, InstrumentName='Triangle', DifficultyId=1),
                InstrumentRow(InstrumentId=3, InstrumentName='Trumpet', DifficultyId=2),
                InstrumentRow(InstrumentId=4, InstrumentName='Upright Bass', DifficultyId=2)
            ]
        )

if __name__ == '__main__':
    # silence python errors when user runs program
    with open(os.devnull, 'w') as stderr, redirect_stderr(stderr):
        unittest.main()