import React from 'react';
import PropTypes from 'prop-types';
import './ProductDetail.css';

const ProductDetail = ({ product }) => {
    return (
        <div className="product-detail">
            <h1>{product.name}</h1>
            <img src={product.image} alt={product.name} />
            <p>{product.description}</p>
            <h2>${product.price.toFixed(2)}</h2>
            <button>Add to Cart</button>
        </div>
    );
};

ProductDetail.propTypes = {
    product: PropTypes.shape({
        name: PropTypes.string.isRequired,
        image: PropTypes.string.isRequired,
        description: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
    }).isRequired,
};

export default ProductDetail;