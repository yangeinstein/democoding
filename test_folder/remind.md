# 图书管理系统使用说明

## 中文版

### 系统概述
这是一个简单的图书管理系统，使用Python的Flask框架作为后端，HTML和CSS作为前端。系统不需要连接数据库，而是使用JSON文件来存储图书信息。

### 主要功能
1. **查看图书**：浏览所有图书的列表，包括书名、作者、出版年份和借阅状态。
2. **添加图书**：向系统中添加新的图书记录。
3. **借出图书**：记录借阅人信息和借阅期限，系统会自动计算预计归还日期。
4. **归还图书**：将已借出的图书标记为已归还状态。
5. **删除图书**：从系统中永久删除图书记录。

### 技术实现
- **后端**：Python Flask框架
- **前端**：HTML, CSS
- **数据存储**：JSON文件（books.json）
- **部署方式**：本地运行，无需数据库

### 如何运行
1. 确保已安装Python和Flask（`pip install flask`）
2. 在命令行中导航到项目文件夹
3. 运行命令：`python app.py`
4. 在浏览器中访问：`http://127.0.0.1:5000/`

### 文件结构
```
/test_folder
  /static
    /css
      style.css
  /templates
    layout.html
    index.html
    add_book.html
    view_books.html
    borrow_book.html
  app.py
  books.json
```

### 注意事项
- 系统使用JSON文件存储数据，重启应用后数据不会丢失
- 系统适合小型图书管理场景，不适合大规模使用
- 没有用户认证功能，所有人都可以执行所有操作

---

# Library Management System User Guide

## English Version

### System Overview
This is a simple library management system built with Python's Flask framework as the backend and HTML/CSS as the frontend. The system doesn't require a database connection, instead using a JSON file to store book information.

### Main Features
1. **View Books**: Browse a list of all books, including title, author, publication year, and borrowing status.
2. **Add Books**: Add new book records to the system.
3. **Borrow Books**: Record borrower information and loan period, with the system automatically calculating the expected return date.
4. **Return Books**: Mark borrowed books as returned.
5. **Delete Books**: Permanently remove book records from the system.

### Technical Implementation
- **Backend**: Python Flask framework
- **Frontend**: HTML, CSS
- **Data Storage**: JSON file (books.json)
- **Deployment**: Local running, no database required

### How to Run
1. Ensure Python and Flask are installed (`pip install flask`)
2. Navigate to the project folder in the command line
3. Run the command: `python app.py`
4. Access in browser: `http://127.0.0.1:5000/`

### File Structure
```
/test_folder
  /static
    /css
      style.css
  /templates
    layout.html
    index.html
    add_book.html
    view_books.html
    borrow_book.html
  app.py
  books.json
```

### Notes
- The system uses a JSON file to store data, so data will not be lost after restarting the application
- The system is suitable for small-scale library management scenarios, not for large-scale use
- There is no user authentication functionality, so anyone can perform all operations