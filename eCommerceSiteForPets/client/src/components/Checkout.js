import React, { useState } from 'react';

const Checkout = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        address: '',
        city: '',
        state: '',
        zip: '',
        paymentMethod: 'creditCard'
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle form submission logic here
        console.log('Form submitted:', formData);
    };

    return (
        <div className="checkout-container">
            <h2>Checkout</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Name:</label>
                    <input type="text" name="name" value={formData.name} onChange={handleChange} required />
                </div>
                <div>
                    <label>Email:</label>
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                </div>
                <div>
                    <label>Address:</label>
                    <input type="text" name="address" value={formData.address} onChange={handleChange} required />
                </div>
                <div>
                    <label>City:</label>
                    <input type="text" name="city" value={formData.city} onChange={handleChange} required />
                </div>
                <div>
                    <label>State:</label>
                    <input type="text" name="state" value={formData.state} onChange={handleChange} required />
                </div>
                <div>
                    <label>Zip Code:</label>
                    <input type="text" name="zip" value={formData.zip} onChange={handleChange} required />
                </div>
                <div>
                    <label>Payment Method:</label>
                    <select name="paymentMethod" value={formData.paymentMethod} onChange={handleChange}>
                        <option value="creditCard">Credit Card</option>
                        <option value="paypal">PayPal</option>
                    </select>
                </div>
                <button type="submit">Complete Purchase</button>
            </form>
        </div>
    );
};

export default Checkout;