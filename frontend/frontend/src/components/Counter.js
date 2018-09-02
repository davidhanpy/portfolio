import React, {Component} from 'react';

class Counter extends Component {
  render() {
    return (
      <div>
        <button onClick={this.handleMinus}>-</button>
        <input type="number" value={this.props.count}/>
        <button onClick={this.handlePlus}>+</button>
      </div>
    );
  }
  handleMinus = () => {
    this.props.changeCount(this.props.count - 1);
  }
  handlePlus = () => {
    this.props.changeCount(this.props.count + 1);
  }
}

export default Counter;