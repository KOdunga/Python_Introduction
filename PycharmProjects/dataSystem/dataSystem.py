from flask import Flask,render_template,Response,request # The render comment helps to be able to render our html, Responce is for the graph, request is for post / get operations
import pandas
import psycopg2
import pygal
import seaborn
import matplotlib
from pygal.style import Style



app = Flask(__name__)
#Create a global connection to the db
conn = psycopg2.connect(database = "modcom_db",
                            user = "postgres",
                            password="password",
                            host= "localhost",
                            port="5432")


@app.route('/')                 # slash (/) is the main route. This is the homepage route
def hello_world():
    return render_template("home.html")  #We return our template


@app.route("/aboutus")
def about():
    return render_template("about.html")


@app.route("/contacts")
def contacts():
    return render_template("graph1.html")



@app.route("/graph1")         # We draw a pie chart graph and render it to contacts page using pygal
def graph1():
    pie = pygal.Pie()
    pie.title = "COMPUTERS MARKET SHARE 2018"
    pie.add("HP", 20)
    pie.add("DELL", 50)
    pie.add("LENOVO", 30)
    return Response(response=pie.render(),content_type='image/svg+xml') # svg is Scalar vector graphics i.e 2D. This is just a responce, we are
                                                                          #not rendering like before

# To draw a graph from a database connection

@app.route("/graphdb")         # We draw a pie chart graph and render it to contacts page using pygal
def graphdb():
    custom_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#53E89B',
        foreground_strong='#53A0E8',
        foreground_subtle='#630C0D',
        opacity='.6',
        opacity_hover='.9',
        transition='400ms ease-in',
        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))

    dataframe = pandas.read_sql_query("SELECT count(gender),gender FROM emp_details GROUP BY gender",conn) # Pull the database data
    print (dataframe)

    pie = pygal.Pie(Style = custom_style)
    pie.title = "GENDER DISTRIBUTION IN %"
    pie.add(dataframe['gender'].tolist()[0], dataframe['count'].tolist()[0])
    pie.add(dataframe['gender'].tolist()[1], dataframe['count'].tolist()[1])

    return Response(response=pie.render(),content_type='image/svg+xml') # svg is Scalar vector graphics i.e 2D. This is just a responce, we are
                                                                          #not rendering like before


@app.route("/graphdbar")         # We draw a pie chart graph and render it to contacts page using pygal
def graphdbar():

    dataframe = pandas.read_sql_query("SELECT count(gender),gender FROM emp_details GROUP BY gender",conn) # Pull the database data
    #print (dataframe)

    #pie = pygal.Bar()
    pie= pygal.HorizontalBar()
    pie.title = "GENDER DISTRIBUTION IN %"
    pie.add(dataframe['gender'].tolist()[1], dataframe['count'].tolist()[1])
    pie.add(dataframe['gender'].tolist()[0], dataframe['count'].tolist()[0])


    return Response(response=pie.render(),content_type='image/svg+xml') # svg is Scalar vector graphics i.e 2D. This is just a responce, we are
                                                                          #not rendering like before

@app.route("/graphline") #Graphing a line graph from db
def graphline():
    dataframe = pandas.read_sql_query("SELECT emp_details.idno ,emp_details.dob, emp_salary.amount, emp_salary.pay_date FROM emp_details INNER JOIN  emp_salary ON emp_details.idno = emp_salary.idno ",conn)
    print dataframe



    line_chart = pygal.Line()
    line_chart = pygal.StackedLine(fill=True)
    line_chart.title = 'Employee Loan Repayment'
    line_chart.x_labels = dataframe ['dob'].tolist()
    line_chart.add('AMOUNT',dataframe['amount'].tolist())
    line_chart.add('IDNO',dataframe['idno'].tolist())
    #line_chart.add(dataframe['pay_date'].tolist())

    return Response(response=line_chart.render(), content_type='image/svg+xml')





@app.route("/graph2")
def graph2():
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    return Response(response=line_chart.render(), content_type='image/svg+xml')
    #line_chart.render()

@app.route("/graph4")
def graph4():
    radar_chart = pygal.Radar()
    radar_chart.title = 'V8 benchmark results'
    radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay',
                            'NavierStokes']
    radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
    radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
    radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
    return Response(response=radar_chart.render(), content_type='image/svg+xml')

@app.route("/graph3")
def graph3():
    line_chart = pygal.Bar()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    return Response(response=line_chart.render(), content_type='image/svg+xml')



@app.route("/details")       # you will also require pandas to handle python data
def details():              # pip install psycopg2 to help in database connectivity, a database adapter



        # the slash \ is used to break code into two lines
            #We use pandas to read the sql and pass the connection

    # dataframe = pandas.read_sql_query("SELECT * FROM emp_details",conn)

    #dataframe = pandas.read_sql_query("SELECT * FROM emp_details",conn)

    #dataframe = pandas.read_sql_query("SELECT dob, fname FROM emp_details where gender = 'M'",conn)

    #dataframe = pandas.read_sql_query("SELECT dob, lname,date_joined "
       #                               "FROM emp_details where date_joined "
            #                          "BETWEEN  '1988-01-01' and '1993-12-12' ORDER BY date_joined ASC ", conn)

    #dataframe = pandas.read_sql_query("SELECT dob, lname,date_joined "
       #                               "FROM emp_details where date_joined "
         #                             "BETWEEN  '1988-01-01' and '1993-12-12' ORDER BY date_joined ASC LIMIT 3", conn)

    dataframe = pandas.read_sql_query("SELECT * FROM emp_details where gender = 'F' LIMIT 20", conn)
    print (dataframe)
    return render_template('details.html',data = dataframe) # when you go to return the data, pass is along in the return statement
                                                        # In html, you will deal with the data input. You can pass several other variables
                                                        # under whatever name you want.
                                                        # Data becomes availabl in the template it has been rendered to using jinja


@app.route("/male_salaries")
def male_salaries():
    #dataframe = pandas.read_sql_query("SELECT * FROM emp_salary ", conn)
    dataframe = pandas.read_sql_query("SELECT emp_details.fname,emp_details.lname,emp_details.gender,emp_salary.amount  FROM emp_details FULL OUTER JOIN emp_salary ON emp_details.idno=emp_salary.idno WHERE emp_details.gender = 'F' and emp_salary.amount is not NULL ", conn)
    return render_template('salaries.html',output = dataframe)

@app.route("/analysis")
def analysis():
    dataframe = pandas.read_sql_query("SELECT * FROM emp_salary", conn)  #This is for reading from mysql
    #dataframe = pandas.read_excel # If you want to read from excel.You can also read from a microsoft db or any other db.

    # Selecting a specific column
    #print (dataframe['fname'].tolist()) # Convert a specific column to be a list
    #print(dataframe['amount'].mean())
    #print(dataframe['amount'].describe())
    #print(dataframe.shape) #Number of columns and rows of a table
    #print(dataframe.ndim) # table dimension
    #print(dataframe['fname'].tail(20)) #select the last 20 first names
    print(dataframe.head(n=5)) # brings the top n entries of the table. Tail brings the last n function


@app.route("/courses")          # pointing to the route
def school_courses():           # the name of the function
    return "Music"


@app.route("/save",methods=['POST','GET'])  # You need to pass both post and get instructions here
def save():
    if request.method == 'POST':        # This is for the first time that you show the user the form, there is no data to submit. just pass and load the form
        cursor = conn.cursor()          # Create a cursor object. The cursor is used to excute the queries in mysql. Before we were using pandas

        sql = "INSERT INTO emp_details VALUES (%s,%s,%s,%s,%s,%s)"     # For mysql, you can ignore the exact values if you are going to insert all the values. If you are dealing with specific column only, then you will need to mention them.
     # Anything you get from a form is a string. If you want integers, you have to cnvert it.
     # Values %s is used to prevent injection. Ensures that python only expects 5 values.


        # PREPARE DATA TO SAVE
        idno = request.form['idno']
        dob = request.form['dob']
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        date_joined = request.form['date_joined']

        # EXECUTE THE QUERY
        cursor.execute(sql,(idno,dob,fname,lname,gender,date_joined))

        #COMMIT THE CHANGES
        conn.commit()
        return render_template('save.html',msg = "Saved. Enter another record to save.") # This will only show if the commit is a sucess. Important for ensuring data has been saved.


    else:
        return  render_template('save.html')


# Using Pandas to do a search.

@app.route("/search",methods=['POST','GET'])
def search():
    if request.method == 'POST':
        idno = request.form['idno']
        #gender = request.form['gender']
        dataframe = pandas.read_sql_query("SELECT * FROM emp_details WHERE idno=%s",conn,params = [idno])  #If you want to pass it as an integer use %d
        #dataframe = pandas.read_sql_query("SELECT * FROM emp_details WHERE gender=%s", conn, params=[gender])
        print (dataframe)
        return render_template('search.html',msg = "Record Found")
    else:
        return  render_template('search.html')

@app.route("/search_gender", methods=['POST', 'GET'])
def searchgender():
    if request.method == 'POST':

        gender = request.form['gender'].upper()

        dataframe = pandas.read_sql_query("SELECT * FROM emp_details WHERE gender=%s", conn, params=[gender])

        line_chart = pygal.StackedLine()
        line_chart.title = 'Employee GENDER GRAPH'
        line_chart.x_labels = dataframe['dob'].tolist()
        line_chart.add('ID Number', dataframe['idno'].tolist())

        return Response(response=line_chart.render(), content_type='image/svg+xml')

        #return render_template('search_gender.html')
    else:
        return render_template('search_gender.html')





        #@app.route("/search",methods=['POST','GET'])
#def search():
 #   if request.method == 'POST':
  #      cursor = conn.cursor()
   #     sql = "SELECT * FROM emp_details WHERE idno = %s "
    #    idno = str(request.form['idno'])
     #   print (type(idno))
      #  #cursor.execute(sql,(idno))
       # cursor.execute(sql,(str(idno)))
        #row = cursor.fetchone()
    #    print (row)
    #    conn.commit()
    #    return render_template('search.html',msg = "Record Found")
    #else:
     #   return  render_template('search.html')



@app.route("/mydata/<id>")              # Routes can accept variables. Here, id is a variable passed to the route
def my_data(id):                          # Pass the id into th function here
    return "this",str(id)

if __name__ == '__main__':
    app.run(debug =True,port= 8000)        #Debug ensures that changes take effect immediately, you dont have to keep on running afresh
                        # You can always change the port number if your port is busy for the flask connection




# Homework: Select records, return to a template called salaries and display on website.
# Display loans also.
#Try using joins


# Quiz
# Create a form to allow for searching and returning a record. Search by ID. Just have a single input form.
# sql = "SELECT FROM where idno == "