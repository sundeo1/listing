import React, { useState } from 'react';
import axios from 'axios';
import Loader from 'react-loader-spinner';
import PropTypes from 'prop-types';

const ListingForm = (props) => {
    const [formData, setFormData] = useState({
        category: 'Others',
        price: '0+',
        days_listed: '1 or less',
        has_photos: '1+',
        keywords: ''
    });

    const {  category, price, days_listed, has_photos, keywords } = formData;

    const [loading, setLoading] = useState(false);

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };

        setLoading(true);
        axios.post('http://127.0.0.1:8000/api/listings/search', {  category,price,days_listed, has_photos, keywords }, config)
        .then(res => {
            setLoading(false);
            props.setListings(res.data);
            window.scrollTo(0, 0);
        })
        .catch(err => {
            setLoading(false);
            window.scrollTo(0, 0);
        })
    };

    return (
        <form className='listingform' onSubmit={e => onSubmit(e)}>
            <div className='row'>
            <div className='col-1-of-6'>
                    <div className='listingform__section'>
                        <label className='listingform__label' htmlFor='category'>Category</label>
                        <select className='listingform__select' name='category' onChange={e => onChange(e)} value={category}>
                            <option>Livestock</option>
                            <option>Food</option>
                            <option>Fashion</option>
                            <option>Others</option>
                        </select>
                    </div>
                </div>

                <div className='col-1-of-6'>
                    <div className='listingform__section'>
                        <label className='listingform__label' htmlFor='price'>Minimum Price</label>
                        <select className='listingform__select' name='price' onChange={e => onChange(e)} value={price}>
                            <option>0+</option>
                            <option>200,000+</option>
                            <option>400,000+</option>
                            <option>600,000+</option>
                            <option>800,000+</option>
                            <option>1,000,000+</option>
                            <option>1,200,000+</option>
                            <option>1,500,000+</option>
                            <option>Any</option>
                        </select>
                    </div>
                </div>
                <div className='col-1-of-6'>
                    <div className='listingform__section'>
                        <label className='listingform__label' htmlFor='days_listed'>Days Listed</label>
                        <select className='listingform__select' name='days_listed' onChange={e => onChange(e)} value={days_listed}>
                            <option>1 or less</option>
                            <option>2 or less</option>
                            <option>5 or less</option>
                            <option>10 or less</option>
                            <option>20 or less</option>
                            <option>Any</option>
                        </select>
                    </div>
                    </div>
                


                <div className='col-1-of-6'>
                    <div className='listingform__section'>
                        <label className='listingform__label' htmlFor='keywords'>Keywords</label>
                        <input className='listingform__input' name='keywords' type='text' onChange={e => onChange(e)} value={keywords} />
                    </div>
                </div>


                <div className='col-1-of-6'>
                    {loading ?
                        <div className='listingform__loader'>
                            <Loader
                                type="Oval"
                                color="#424242"
                                height={50}
                                width={50}
                            />
                        </div> : 
                        <button className='listingform__button listingform__button--primary'>Save</button>
                    }
                </div>
            </div>
        </form>
    );
};

ListingForm.propTypes = {
    setListings: PropTypes.func.isRequired
};

export default ListingForm;
