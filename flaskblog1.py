from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, SearchForm
from bp import Node, BplusTree
from os import listdir
import ctypes
import math
import os

def printTree(tree):
    lst = [tree.root]
    level = [0]
    leaf = None
    flag = 0
    lev_leaf = 0
    data=""

    node1 = Node(str(level[0]) + str(tree.root.values))

    while (len(lst) != 0):
        x = lst.pop(0)
        lev = level.pop(0)
        if (x.is_leaf == False):
            for i, item in enumerate(x.keys):
                data=data.join(item.values)
                data=data+"\n"
                with open('bp.txt', 'a+') as f:
                    f.write(data)
                    f.write("\n")
                # print(item.values)
        else:
            for i, item in enumerate(x.keys):
                data=data.join(item.values)
                with open('bp.txt', 'a+') as f:
                    f.write(data)
                    f.write("\n")
                # print(item.values)
            if (flag == 0):
                lev_leaf = lev
                leaf = x
                flag = 1

# # def printTree(tree):
# #     lst = [tree.root]
# #     level = [0]
# #     leaf = None
# #     flag = 0
# #     lev_leaf = 0

# #     node1 = Node(str(level[0]) + str(tree.root.values))

# #     while (len(lst) != 0):
# #         x = lst.pop(0)
# #         lev = level.pop(0)
# #         if (x.is_leaf == False):
# #             for i, item in enumerate(x.keys):
# #                 print(item.values)
# #         else:
# #             for i, item in enumerate(x.keys):
# #                 print(item.values)
# #             if (flag == 0):
# #                 lev_leaf = lev
# #                 leaf = x
# #                 flag = 1



# record_len = 3
# bplustree = BplusTree(record_len)
# bplustree.insert('0', '0')
# bplustree.insert('15', '24')
# bplustree.insert('25', '14')
# bplustree.insert('35', '33')
# bplustree.insert('45', '11')
# bplustree.insert('53', '314')
# bplustree.insert('115', '224')
# bplustree.insert('215', '134')
# bplustree.insert('335', '334')
# bplustree.insert('125', '115')
# bplustree.insert('52', '314')
# bplustree.insert('125', '244')
# bplustree.insert('253', '134')
# bplustree.insert('354', '323')
# bplustree.insert('455', '111')
# printTree(bplustree)
# if(bplustree.find()):
#     print("FOUND")
# else:
#     print("~FOUND")

########################################################ENDING################################################################


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'dairy_name': 'sl dairy',
        'product_name': 'PANNER',
        'id1': 'id-1',
        'price': '20'
    },
    {
        'dairy_name': 'sl dairy',
        'product_name': 'PANNER',
        'id1': 'id-2',
        'price': '25'
    },
    {
       'dairy_name': 'sl dairy',
        'product_name': 'PANNER',
        'id1': 'id-3',
        'price': '26'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method=='POST':
        inputf=str(form.id1.data)+"|"+str(form.productname.data)+"|"+str(form.dairyname.data)+"|"+str(form.price.data)
        for i in range(len(inputf),50):
            inputf+='|'
        inputf+='\n'
        detail=str(form.id1.data)+"\n"
        with open('id.txt','a+') as f1:
            f1.write(detail)
        with open('d1.txt', 'a+') as f:
            f.write(inputf)
        flash(f'{form.productname.data} added!', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)


@app.route("/search", methods=['GET', 'POST'])
def search():
    record_len = 3
    counter=0
    str1=""
    f=open('bp.txt','a+')
    bplustree = BplusTree(record_len)
    form = SearchForm()
    if request.method=='POST':
        reader=open('id.txt','r') 
        line=reader.readlines()
        converted_list = []
        for element in line:
            converted_list.append(element.strip())
        flash(f'{converted_list} choose id from these values!','success')
        for ele in converted_list:
            bplustree.insert(ele,counter)
        printTree(bplustree)
        inp=str(form.id1.data)
        filename = 'd1.txt'
        val1=int(inp)-1
        if(bplustree.find(inp)):
            with open(filename) as fh:
                fh.seek((val1*52), os.SEEK_SET)
                row = fh.readline()
                flash(f'{row}','success')       
            flash(f'found!','success')
        else:
            flash(f'~added!','success')
        # file_variable = open('id.txt')
        #all_lines_variable = file_variable.readlines()
        #flash(all_lines_variable[form.id1.data - 1],'success')
    return render_template('search.html', title='search', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('register'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
