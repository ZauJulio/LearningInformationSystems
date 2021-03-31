const path = require('path');
const withImages = require('next-images')
module.exports = withImages({
  ignoreTypes: ["svg"],
  webpack(config, options) {
    return config
  },
  env: {
    API_KEY: process.env.API_KEY,
  },
})