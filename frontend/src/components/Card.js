import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';

const card = (props) => {
    const numberWithCommas = (x) => {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    };

    return (
        <div className='card'>
            <h3 className='card__title'>{props.title}</h3>
            <div className='card__header'>
                <img className='card__header__photo' src={props.photo_main} alt='House' />
            </div>
            <p className='card__location'>{props.address}, {props.city}</p>
            <div className='row'>
                {/* <div className='col-3-of-3'>
                <p className='card__info'>Category: {props.category}</p>
                </div> */}
                <div className='col-2-of-3'>
                    <p className='card__info'>Price: UGX {numberWithCommas(props.price)}</p>
                </div>
            </div>
            <Link className='card__link' to={`/listings/${props.slug}`}>View Details</Link>
        </div>
    );
};

card.propTypes = {
    title: PropTypes.string.isRequired,
    photo_main: PropTypes.string.isRequired,
    address: PropTypes.string.isRequired,
    city: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    slug: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
};

export default card;
