from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# 初始化一些示例图书
books = [
    {"id": 1, "title": "三体", "author": "刘慈欣", "year": 2008, "available": True, "borrower": None, "borrow_date": None, "return_date": None},
    {"id": 2, "title": "活着", "author": "余华", "year": 1993, "available": True, "borrower": None, "borrow_date": None, "return_date": None},
    {"id": 3, "title": "百年孤独", "author": "加西亚·马尔克斯", "year": 1967, "available": False, "borrower": "张三", "borrow_date": "2023-10-01", "return_date": "2023-10-30"}
]

# 保存和加载图书数据
def save_books():
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def load_books():
    global books
    if os.path.exists('books.json'):
        with open('books.json', 'r', encoding='utf-8') as f:
            books = json.load(f)

# 尝试加载已有的图书数据
try:
    load_books()
except:
    # 如果加载失败，使用默认图书并保存
    save_books()

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/books')
def view_books():
    return render_template('view_books.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # 获取表单数据
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')
        
        # 简单验证
        if not title or not author or not year:
            flash('请填写所有字段')
            return redirect(url_for('add_book'))
        
        # 创建新书
        new_id = max([book['id'] for book in books], default=0) + 1
        new_book = {
            "id": new_id,
            "title": title,
            "author": author,
            "year": int(year),
            "available": True,
            "borrower": None,
            "borrow_date": None,
            "return_date": None
        }
        
        # 添加到列表并保存
        books.append(new_book)
        save_books()
        flash('图书添加成功！')
        return redirect(url_for('view_books'))
    
    return render_template('add_book.html')

@app.route('/borrow/<int:book_id>', methods=['GET', 'POST'])
def borrow_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        flash('图书不存在！')
        return redirect(url_for('view_books'))
    
    if not book['available']:
        flash('该图书已被借出！')
        return redirect(url_for('view_books'))
    
    if request.method == 'POST':
        borrower = request.form.get('borrower')
        days = int(request.form.get('days', 30))
        
        if not borrower:
            flash('请输入借阅人姓名')
            return redirect(url_for('borrow_book', book_id=book_id))
        
        # 更新图书信息
        book['available'] = False
        book['borrower'] = borrower
        book['borrow_date'] = datetime.now().strftime('%Y-%m-%d')
        
        # 计算预计归还日期
        return_date = datetime.now() + timedelta(days=days)
        book['return_date'] = return_date.strftime('%Y-%m-%d')
        
        save_books()
        flash(f'《{book["title"]}》已成功借出给{borrower}，预计归还日期：{book["return_date"]}')
        return redirect(url_for('view_books'))
    
    return render_template('borrow_book.html', book=book)

@app.route('/return/<int:book_id>', methods=['GET', 'POST'])
def return_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        flash('图书不存在！')
        return redirect(url_for('view_books'))
    
    if book['available']:
        flash('该图书未被借出！')
        return redirect(url_for('view_books'))
    
    # 更新图书信息
    book['available'] = True
    borrower = book['borrower']
    book['borrower'] = None
    book['borrow_date'] = None
    book['return_date'] = None
    
    save_books()
    flash(f'《{book["title"]}》已由{borrower}归还成功！')
    return redirect(url_for('view_books'))

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    save_books()
    flash('图书已删除！')
    return redirect(url_for('view_books'))

if __name__ == '__main__':
    app.run(debug=True)