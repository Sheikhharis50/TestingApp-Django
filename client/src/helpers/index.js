/**
 * Return URL combined with query parameters
 * @param {string} url - base URL
 * @param {dictionary} data - query parameter in dictionary form
 * @returns {string}
 */
export function encodeParamsToURI(url, data) {
    let param;
    try {
        param = !isEmptyObj(data) ? `?${Object.keys(data)
            .map((k) => {
                // NOTE: %2B replacement logic has been added to prevent problem that occurs when
                //       there is a "+" string inside the search query. This is a temporary fix.
                return `${encodeURIComponent(k)}=${encodeURIComponent(data[k]).replace(
                    /%2B/g,
                    "+"
                )}`
            })
            .join("&")}` : ""
    } catch (error) { }

    return `${url}${param}`
}

/**
 * @param {dictionary} obj
 * @returns {bool}
 */
export function isEmptyObj(obj) {
    for (var key in obj) {
        if (obj.hasOwnProperty(key)) return false
    }
    return true
}