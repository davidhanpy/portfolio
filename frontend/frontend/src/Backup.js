import React, { Component } from 'react';
import Counter from './components/Counter';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      list: [],
    }
    console.log('constructor');
  }
  componentDidMount() {
    console.log('did mount');
  }
  shouldComponentUpdate(nextProps, nextState) {
    console.log(this.state.list, nextState);
    if(this.state.list.length !== nextState.list.length)
      return true;
    else
      return false;
  }
  componentWillUpdate() {
    console.log('will update');
  }
  componentDidUpdate() {
    console.log('did update');
  }
  render() {
    console.log('render');
    const listElements = this.state.list.map((item, idx) => {
      return <p key={idx}>{item}</p>
    })
    return (
      <div className="App">
        <button onClick={this.handleClick}>Add</button>
        {listElements}
      </div>
    );
  }
  handleClick = () => {
    const newArr = Array.from(this.state.list);
    newArr.push('Hello World');
    this.setState({list: newArr});
    // console.log(this.state.list);
  }
}

export default App;
