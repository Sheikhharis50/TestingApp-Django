import { DEBUG } from '../config';

const print = (message = "", level = 'error') => {
    const LOG_TYPE = {
        'error': console.error,
        'warn': console.warn,
        'log': console.log,
        'info': console.info,
    }
    const selective = LOG_TYPE[level]
    DEBUG || selective(message);
}

const log = (message) => { print(message, 'log') }
const error = (message) => { print(message, 'error') }
const info = (message) => { print(message, 'info') }
const warn = (message) => { print(message, 'warn') }

export { log, error, info, warn }