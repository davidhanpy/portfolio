//템플릿 컴포넌트 생성
//먼저 틀부터 생성
import React from 'react';
import './TodoListTemplate.css';

//css에서 import해서(이거은 상속이 아니라?) 추후에 받을 form, children을 넣어줄 것인가?  

const TodoListTemplate = ({form, children}) => {
    return (
        <main className="todo-list-template">
        <div className="title">
        오늘 할 일
        </div>
        <section className="form-wrapper">
        { form }
        </section>
        <section className="todos-wrapper">
        { children }
        </section>
        </main>
    );
};

export default TodoListTemplate;
//export default이 행위는 무엇인가?
//what is 비구조화할당?
//함수형 컴포넌트?
