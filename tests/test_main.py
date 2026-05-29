**Pytest uchun test kodini quyidagicha yozing:**

```python
import pytest
from todo_list import TodoList

def test_todo_list_init():
    todo_list = TodoList()
    assert todo_list.tasks == []

def test_add_task():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    assert todo_list.tasks == ["Task 1"]

def test_add_multiple_tasks():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    assert todo_list.tasks == ["Task 1", "Task 2"]

def test_remove_task():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.remove_task("Task 1")
    assert todo_list.tasks == []

def test_remove_task_not_found():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.remove_task("Task 2")
    assert todo_list.tasks == ["Task 1"]

def test_remove_multiple_tasks():
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    todo_list.remove_task("Task 1")
    assert todo_list.tasks == ["Task 2"]
```

**Jest uchun test kodini quyidagicha yozing:**

```javascript
import TodoList from './todo-list';

describe('TodoList', () => {
  it('should initialize with an empty list', () => {
    const todoList = new TodoList();
    expect(todoList.tasks).toEqual([]);
  });

  it('should add a task to the list', () => {
    const todoList = new TodoList();
    todoList.addTask('Task 1');
    expect(todoList.tasks).toEqual(['Task 1']);
  });

  it('should add multiple tasks to the list', () => {
    const todoList = new TodoList();
    todoList.addTask('Task 1');
    todoList.addTask('Task 2');
    expect(todoList.tasks).toEqual(['Task 1', 'Task 2']);
  });

  it('should remove a task from the list', () => {
    const todoList = new TodoList();
    todoList.addTask('Task 1');
    todoList.removeTask('Task 1');
    expect(todoList.tasks).toEqual([]);
  });

  it('should not remove a task that does not exist', () => {
    const todoList = new TodoList();
    todoList.addTask('Task 1');
    todoList.removeTask('Task 2');
    expect(todoList.tasks).toEqual(['Task 1']);
  });

  it('should remove multiple tasks from the list', () => {
    const todoList = new TodoList();
    todoList.addTask('Task 1');
    todoList.addTask('Task 2');
    todoList.removeTask('Task 1');
    expect(todoList.tasks).toEqual(['Task 2']);
  });
});
```
