const defaultEnvironment = 'dev'
const environment = {
  production: {
    apiUrl: 'https://',
  },
  dev: {
    apiUrl:'http://localhost:5000'
  }
}

export default environment[defaultEnvironment]