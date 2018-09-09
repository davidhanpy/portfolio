import React, { Component } from 'react';
import './TodoItem.css';
//onClick={(e)}이것은 객체 변수?
//$및 && 약간 헷갈림..
//<div className={`todo-text ${checked && 'checked'}`}>
//onToggle?
//stopPropagation()메소드?
//props를 전달받는다.. 즉 다양한 형태의 변수 혹은 객체(함수)를 전달받는다고 생각하면 되나?
//onToggle과 onRemove 는 id 를 파라미터로 넣으면 해당 id 를 가진 데이터를 업데이트합니다. 파라미터를 넣어줘야 하기 때문에, 이 과정에서 우리는 onClick={() => onToggle(id)} 와 같은 형식으로 작성을 했는데요, onClick={onToggle{id}} 와 같은 형식으로 하고 싶다면.. 절대 안됩니다!! 리액트가 초심자가 한번 쯤 할 수 있는 실수입니다. 이렇게 하면 해당 함수가 렌더링 될 때 호출이 됩니다. 해당 함수가 호출되면 데이터가 변경 될 것이고, 데이터가 변경되면 또 리렌더링이 되겠죠? 그러면 또 이 함수가 호출되고.. 무한 반복입니다.
//`백쿼트? <div className={`todo-text ${checked && 'checked'}`}> 자세히 공부를..해야..
//데이터의 구체적인.. 행방을 표현주는 컴포넌트?
class TodoItem extends Component {
    render() {
        const { text, checked, id, onToggle, onRemove } = this.props;

        return (
            <div className="todo-item" onClick={() => onToggle(id)}>
            <div className="remove" onClick={(e) => {e.stopPropagation(); onRemove(id)}}>&times;</div>
            
            <div className={`todo-text ${checked && 'checked'}`}>
            {/* checked === true?'checked':'' */}
            <div>{text}</div>
            </div>
            {
                checked && (<div className="check-mark">v</div>)
            }
            </div>
        );
    }
}

export default TodoItem;