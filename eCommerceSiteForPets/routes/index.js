const express = require('express');
const router = express.Router();

// Import controllers
const productController = require('../controllers/productController');
const userController = require('../controllers/userController');
const orderController = require('../controllers/orderController');

// Product routes
router.get('/products', productController.getAllProducts);
router.get('/products/:id', productController.getProductById);
router.post('/products', productController.createProduct);
router.put('/products/:id', productController.updateProduct);
router.delete('/products/:id', productController.deleteProduct);

// User routes
router.post('/users/register', userController.registerUser);
router.post('/users/login', userController.loginUser);
router.get('/users/:id', userController.getUserById);

// Order routes
router.post('/orders', orderController.createOrder);
router.get('/orders/:id', orderController.getOrderById);

module.exports = router;