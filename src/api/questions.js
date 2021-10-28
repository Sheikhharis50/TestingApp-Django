import { error } from '../services/makeLogger';
import makeRequest from '../services/makeRequest';

export const getQuestions = async () => {
    try {
        const { response } = await makeRequest("questions").get()
        return response
    } catch (err) {
        error(err)
    }
}