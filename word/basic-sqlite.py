#!/user/bin/python3
# Basic sqlite operations modelled from Python3 Essential Training
# Not production quality - no error checking
# production version will have functions in a class and generator functions

import sqlite3
import os

def insert(db, row):
    db.execute('insert into test (t1, i1) value (?, ?)', (row['t1'], row['i1']))
    db.commit()

def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()

def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()

def display_row(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print(' {}:{}'.format(row['t1'], row['i1']))


def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    print('Creating table test')
    print('First removing old test. . .')
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int )')
    print('New test table created')
    print('Creating test data')
    insert(db, dict(t1 = 'one', i1 = 1))
#    insert(db, dict(t1 = 'two', i1 = 2))
#   insert(db, dict(t1 = 'three', i1 = 3))
#    insert(db, dict(t1 = 'four', i1 = 4))
#    display_row(db)

# Reads
    print('Retrieving rows . . . . .')
    print(dict(retrieve(db,'one')), dict(retrieve(db, 'two')))

# Updates
    print('Updating row . . . . .')
    update(db, dict(t1 = 'one', i1 = 111))
    display_row(db)




if __name__ == "__main__": main()
