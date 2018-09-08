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
//컴포넌트상속 받아서 app, 그리고 렌더링
//컴포넌트상속 받아서 렌더링 할때 <~~~> 이런식으로?
//TodoListTemplate form={Form/>}>이부분자세히설명이..
class App extends Component {
  render() {
    return (   
    <TodoListTemplate form={<Form/>}>
        템플릿 완성
      </TodoListTemplate>
    );
  }
}

export default App;