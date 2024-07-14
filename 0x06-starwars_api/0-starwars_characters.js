#!/usr/bin/node


const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
    console.log('Please provide a movie ID as the first argument.');
    process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

axios.get(apiUrl)
    .then(response => {
        const characters = response.data.characters;
        const characterPromises = characters.map(url => axios.get(url).then(res => res.data.name));
        return Promise.all(characterPromises);
    })
    .then(characterNames => {
        characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
        console.error('Error fetching data:', error.message);
    });

