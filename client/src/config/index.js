const PROTOCOL = 'http'
const HOSTNAME = 'localhost:8000'
export const BASE_URL = `${PROTOCOL}://${HOSTNAME}/api/`
export const ENV = process.env.REACT_APP_ENV
export const DEBUG = ENV === "development"

const configs = {
    BASE_URL,
    ENV
}

export default configs;