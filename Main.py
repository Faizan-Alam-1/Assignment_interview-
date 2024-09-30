# Comprehensive Todo App Development Challenge
# Overview
# You are tasked with developing a Todo application backend in Python / JS. This challenge is divided into three levels of increasing complexity. Candidates should attempt the level that best matches their experience and skills. You may progress to higher levels if time permits.
# Level 1: Basic Todo App
# Task Description
# Implement a basic Todo application backend with two main classes: Todo and TodoApp.
# Requirements
       
# Todo Class , Todo
# Attributes: id, title, content, created_at, updated_at
# TodoApp Class Implement the following methods:
# create_Todo(title: str, content: str) -> Todo
# get_Todo(Todo_id: int) -> Todo
# update_Todo(Todo_id: int, title: str = None, content: str = None) -> Todo
# delete_Todo(Todo_id: int) -> bool
# list_Todos() -> List[Todo]
# Additional Requirements
# Implement proper error handling
# Update updated_at timestamp on Todo modifications
# Use type hints and write clear docstrings / comments



from datetime import datetime

class Todo:
    def __init__(self, todo_id, title, content):
        """
        Initializes a new Todo item.
        Attributes: id, title, content, created_at, updated_at 
        """
        self.id = todo_id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = self.created_at


class TodoApp:
    def __init__(self):
        """
        Initializes empty list of Todos.
        """
        self.todos = []
     

    def create_Todo(self, title, content):
        """
        Creates a new Todo item.
        """
        todo = Todo(self.next_id, title, content)
        self.todos.append(todo)
        return todo

    def get_Todo(self, todo_id):
        """
        Retrieves a Todo item by its ID.
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_Todo(self, todo_id, title=None, content=None):
        """
        Updates a Todo item's title and/or content.
        """
        todo = self.get_Todo(todo_id)
        if not todo:
            return None

        if title:
            todo.title = title
        if content:
            todo.content = content
        todo.updated_at = datetime.now()
        return todo

    def delete_Todo(self, todo_id):
        """
        Deletes a Todo item by its ID.

        """
        todo = self.get_Todo(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False

    def list_Todos(self):
        """
        Lists all Todo items.
        return: A list of all Todos
        """
        return self.todos


