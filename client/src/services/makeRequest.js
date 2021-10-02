import makeURL from './makeURL';
import _fetch from 'isomorphic-fetch';

const makeRequest = (url = "", params = {}, data = {}) => {
    const credentials = "include"
    const headers = {
        Accept: "application/json",
        "Content-Type": "application/json",
    }
    const request = async (method) => {
        try {
            url = makeURL(url, params)
            let payload = {
                method: method,
                credentials: credentials,
                headers: headers,
                mode: "cors",
            }
            if (method !== "GET")
                payload = { ...payload, body: JSON.stringify(data) }
            const _res = await _fetch(url, payload)
            const _data = await _res.json()

            if (_res.status === 403) {
            }

            if (!_res.ok) {
                console.error(_res.statusText);
            }

            return {
                state: true,
                response: _data,
            }
        } catch (error) {
            console.error(error);
            return {
                state: false,
                response: error,
            }
        }
    }
    return {
        get: () => { return request("GET") },
        post: () => { return request("POST") },
        patch: () => { return request("PATCH") },
        put: () => { return request("PUT") },
        delete: () => { return request("DELETE") },
    }
}

export default makeRequest;
