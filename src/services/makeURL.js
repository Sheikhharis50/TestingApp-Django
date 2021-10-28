import { BASE_URL } from '../config';
import { encodeParamsToURI } from '../helpers';

const makeURL = (url, params) => {
    return `${BASE_URL}${encodeParamsToURI(url, params)}`
}

export default makeURL;
