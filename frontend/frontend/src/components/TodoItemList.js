import React, { Component } from 'react';
import TodoItem from './TodoItem';
//ref가 뭐죠?
//렌더링할때.. TodoItem(부모)로 부터 먼저 props를 받고.. 그럼 todos는 어디에서?
//this.props?
//아닌가.. Todos를 최상위부모로 부터 받고 난 뒤... todoItem에서 또 import해오는건가?

class TodoItemList extends Component {
    render() {
        const {todos, onToggle, onRemove } = this.props;
        const todoList = todos.map(
            ({id, text, checked}) => (
                <TodoItem
                id={id}
                text={text}
                checked={checked}
                onToggle={onToggle}
                onRemove={onRemove}
                key={id}
                />
            )
        );
        return (
            <div>
            {todoList}
            </div>
        );
    }
}

export default TodoItemList;