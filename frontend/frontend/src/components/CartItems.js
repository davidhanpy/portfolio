import React, {Component} from 'react';
import CartItem from './CartItem';

class CartItems extends Component {
  state = {
    product: [
      { name: 'ABC', price: 5000},
      { name: 'BCD', price: 15000},
      { name: 'CDE', price: 52000},
      { name: 'EDF', price: 3000},
      { name: 'DEF', price: 7000},
    ]
  }
  render() {
    const productElements = this.state.product.map((item, idx) => {
      return (
        <CartItem {...item} key={'product'+idx} />
      )
    })
    return (
      <table>
        <thead>
          <tr>
            <td>이름</td>
            <td>단가</td>
            <td>수량</td>
            <td>총액</td>
          </tr>
        </thead>
        <tbody>
          {productElements}
        </tbody>
      </table>
    )
  }
}

export default CartItems;