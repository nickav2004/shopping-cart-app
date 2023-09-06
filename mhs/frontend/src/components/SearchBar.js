import React from "react";
import { useState } from "react";

function SearchBar(props) {
  const [name, setName] = useState("");
  const [price, setPrice] = useState(0);
  const [type, setType] = useState("");
  const [brand, setBrand] = useState("");

  const searchButtonPressed = () => {
    props.updateSearchParams({ name, price, type, brand });
  };

  return (
    <div className="container">
      <div className="row">
        <h2>Search for Item </h2>
      </div>

      <div className="row">
        <div className="col">
          <label htmlFor="name-field">Name:</label>
          <input
            id="name-field"
            type="text"
            className="form-control"
            value={name}
            onChange={(e) => setName(e.target.value)}
          ></input>
        </div>

        <div className="col">
          <label htmlFor="price-field">Max Price:</label>
          <input
            id="price-field"
            type="number"
            className="form-control"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          ></input>
        </div>

        <div className="col">
          <label htmlFor="type-field">Type:</label>
          <input
            id="type-field"
            type="text"
            className="form-control"
            value={type}
            onChange={(e) => setType(e.target.value)}
          ></input>
        </div>

        <div className="col">
          <label htmlFor="brand-field">Brand:</label>
          <input
            id="brand-field"
            type="text"
            className="form-control"
            value={brand}
            onChange={(e) => setBrand(e.target.value)}
          ></input>
        </div>
      </div>
      <div className="row mt-3">
        <div className="col-4" />

        <button
          className="btn btn-primary col-4"
          type="button"
          onClick={searchButtonPressed}
        >
          Search
        </button>
      </div>
    </div>
  );
}

export default SearchBar;
