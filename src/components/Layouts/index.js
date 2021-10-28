import React from 'react';
import PropTypes from 'prop-types';
import Container from '@mui/material/Container';

const Layout = ({ maxWidth = "xl" }) => {
    return (
        <Container maxWidth={maxWidth}>
            Main
        </Container>
    );
};


Layout.propTypes = {
    maxWidth: PropTypes.string
};


export default Layout;
