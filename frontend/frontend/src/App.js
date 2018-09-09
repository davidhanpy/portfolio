
// import React, { Component } from 'react';
// import CartItems from './components/CartItems';
// import './App.css';

// class App extends Component {
//   render() {
//     return (
//       <div>
//         <CartItems />
//       </div>
//     )
//   }
// }

// export default App;

import React, { Component } from 'react';
import TodoListTemplate from './components/TodoListTemplate';
import Form from './components/Form';
import TodoItemList from './components/TodoItemList';
//컴포넌트상속 받아서 app, 그리고 렌더링
//컴포넌트상속 받아서 렌더링 할때 <~~~> 이런식으로?
//TodoListTemplate form={Form/>}>이부분자세히설명이..
//handlechange, handleCreate, handleKeyPress
//concat 과 push?
//비구조화할당
//handleToggle checked 어떻게 구현?
//target.value의 정확한의미
class App extends Component {

  id=3
  state={
    input:'',
    todos: [
      {id:0, text:'리액트 소개',checked: false},
      {id:1, text:'리액트 소개',checked: true},
      {id:2, text:'리액트 소개',chekced: false}
    ]
  }

  handleChange = (e) => {
    this.setState({
      input: e.target.value
    });
  }

  handleCreate = () => {
    const { input, todos } = this.state;
    this.setState({
      input:'',
      todos:todos.concat({
        id: this.id++,
        text: input,
        checked: false
      })
    })
  }

  handleKeyPress = (e) => {
    if(e.key === 'Enter') {
      this.handleCreate();
    }
  }

  handleToggle = (id) => {
    const {todos} = this.state;
    const index = todos.findIndex(todo => todo.id ===id);
    console.log(index)
    const selected = todos[index];
    console.log(selected)
    const nextTodos = [...todos]; //배열 전체를 복사? - 새 배열에 복사
    console.log(nextTodos) 
    nextTodos[index] = {
      ...selected, //selected의 파라메터들을 컨트롤 한다는뜻?
      checked:!selected.checked //checked를 반전
    };
    console.log(nextTodos[index])

    this.setState({
      todos: nextTodos
    });
  }

  handleRemove = (id) => {
    const { todos } = this.state;
    this.setState({
      todos: todos.filter(todo => todo.id!==id) //새 배열을 filter함수가 리턴해준다.. 새로운 배열을 return한다.
    });
  }
  render() {
    const { input, todos } = this.state;
    const {
      handleChange,
      handleCreate,
      handleKeyPress,
      handleToggle,
      handleRemove
    } = this;

    return (   
    <TodoListTemplate form={(
      <Form
        value={input}
        onKeyPress={handleKeyPress}
        onChange={handleChange}
        onCreate={handleCreate}
      />
    )}>
      <TodoItemList todos={todos} onToggle={handleToggle} onRemove={handleRemove}/>
      {/* 자식 컴포넌트에게 state값을 props로 넘겨준다, 값을 가져오기위한 메소드도 넘겨준다. */}
    </TodoListTemplate>
    );
  }
}

export default App;
