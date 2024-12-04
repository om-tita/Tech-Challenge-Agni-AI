import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { removeFromCart, clearCart } from '../actions/cartActions';

const Cart = () => {
    const cartItems = useSelector(state => state.cart.items);
    const dispatch = useDispatch();

    const handleRemove = (itemId) => {
        dispatch(removeFromCart(itemId));
    };

    const handleClear = () => {
        dispatch(clearCart());
    };

    const totalAmount = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);

    return (
        <div className="cart">
            <h2>Your Shopping Cart</h2>
            {cartItems.length === 0 ? (
                <p>Your cart is empty.</p>
            ) : (
                <div>
                    <ul>
                        {cartItems.map(item => (
                            <li key={item.id}>
                                <span>{item.name} - ${item.price} x {item.quantity}</span>
                                <button onClick={() => handleRemove(item.id)}>Remove</button>
                            </li>
                        ))}
                    </ul>
                    <h3>Total: ${totalAmount.toFixed(2)}</h3>
                    <button onClick={handleClear}>Clear Cart</button>
                </div>
            )}
        </div>
    );
};

export default Cart;