from flask import Flask, request, jsonify
import cx_Oracle
app = Flask(__name__)

books_list = [

    {
        "id": 1,
        "author": "Raghu"
    },
    {
        "id": 2,
        "author": "Rekha"
    },
    {
        "id": 3,
        "author": "Ravi"
    },
    {
        "id": 4,
        "author": "Raju"
    }
]

# try:                               #172.23.214.21  117.192.9.200
#    # cx_Oracle.init_oracle_client(lib_dir=r"/media/shivang/Shivanga/Python/venv/Scripts/youtube/venv/instantclient_21_7")
#     con= cx_Oracle.connect('bio/bio@117.192.9.200:1521/orcl')
#     print('DB Version is + ',con.version)

# except cx_Oracle.DatabaseError as e:
#     print("There is a problem with Oracle", e)

# except Exception as er:
#     print('Error:'+str(er))


@app.route('/')
def initial():
    try:
        con = cx_Oracle.connect('bio/bio@117.192.9.200:1521/orcl')
        print('DB Version is +', con.version)
        return {"message": f"Successfully hit to Database {con.version}"}

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
        return {"message": f"{e}"}

    except Exception as er:
        print('Error:'+str(er))
        return {"message": "DB Error 2"}


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            "Nothing Found", 404

    if request.method == 'POST':
        new_id = request.form['id']
        new_author = request.form['author']

        books_list.append({"id": new_id,
                           "author": new_author})

        return jsonify(books_list), 201


if __name__ == '__main__':
    app.run()
