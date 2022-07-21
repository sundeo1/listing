import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './containers/Home';
import About from './containers/About';
import Contact from './containers/Contact';
import Listings from './containers/Listings';
import ListingDetail from './containers/ListingDetail';
import Login from './containers/Login';
import SignUp from './containers/SignUp';
import NotFound from './components/NotFound';
import Layout from './hocs/Layout';
import PrivateRoute from './components/privateRoute';

import { Provider } from 'react-redux';
import store from './store';

import './sass/main.scss';
import Livestocks from './containers/Livestocks';
import Fashion from './containers/Fashion';
import Food from './containers/Food';
import Others from './containers/Others';
import RealEstate from './containers/RealEstate';

const App = () => (
    <Provider store={store}>
        <Router>
            <Layout>
                <Switch>
                    <Route exact path='/' component={Listings} />
                    <Route exact path='/search' component={Home} />
                    <Route exact path='/livestocks' component={Livestocks} />
                    <Route exact path='/fashion' component={Fashion} />
                    <Route exact path='/others' component={Others} />
                    <Route exact path='/food' component={Food} />
                    <Route exact path='/real-estate' component={RealEstate} />
                    <Route exact path='/about' component={About} />
                    <Route exact path='/contact' component={Contact} />
                    <Route exact path='/listings/:id' component={ListingDetail} />
                    <Route exact path='/login' component={Login} />
                    <Route exact path='/signup' component={SignUp} />
                    <Route component={NotFound} />
                </Switch>
            </Layout>
        </Router>
    </Provider>
);

export default App;
