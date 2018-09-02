import React, {Component} from 'react';
import Counter from './Counter';

class CartItem extends Component {
  state = {
    amount: 0,
    count: 0,
  }
  render() {
    return (
      <tr>
        <td>{this.props.name}</td>
        <td>{this.props.price.toLocaleString()}</td>
        <td><Counter count={this.state.count} changeCount={this.changeCount}/></td>
        <td>{this.state.amount.toLocaleString()}</td>
      </tr>
    );
  }
  changeCount = (number) => {
    if ( number >= 0 )
      this.setState({count: number, amount: number * this.props.price});
  }
}

export default CartItem;
