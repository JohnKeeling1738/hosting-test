// Requiring express for routing
const express = require('express')

// Creating app from express
const app = express()

// Requiring in-built file system
const fs = require('fs')

// GET request which HTML video tag sends


// GET request to the root of the app
app.get('/index.html',function(req,res){

	// Sending index.html file for GET request
	// to the root of the app
})

// Creating server at port 3000
app.listen(3000,function(req,res){
	console.log('Server started at 3000')
})
