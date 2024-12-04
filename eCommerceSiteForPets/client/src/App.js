import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import ProductListing from './components/ProductListing';
import ProductDetails from './components/ProductDetails';
import Cart from './components/Cart';
import Checkout from './components/Checkout';
import Navbar from './components/Navbar';
import './styles/App.css';

const App = () => {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/products" component={ProductListing} />
                    <Route path="/product/:id" component={ProductDetails} />
                    <Route path="/cart" component={Cart} />
                    <Route path="/checkout" component={Checkout} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;