// Helper functions for the eCommerce site for pets

/**
 * Format currency for display
 * @param {number} amount - The amount to format
 * @returns {string} - Formatted currency string
 */
function formatCurrency(amount) {
    return `$${amount.toFixed(2)}`;
}

/**
 * Validate email format
 * @param {string} email - The email to validate
 * @returns {boolean} - True if valid, false otherwise
 */
function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
}

/**
 * Generate a unique ID
 * @returns {string} - Unique ID string
 */
function generateUniqueId() {
    return 'id-' + Math.random().toString(36).substr(2, 16);
}

module.exports = {
    formatCurrency,
    validateEmail,
    generateUniqueId
};