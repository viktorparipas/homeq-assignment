import React from "react";

function ApartmentRow({ apartment }) {
  return (
    <tr>
      <td>{apartment.id}</td>
      <td>{apartment.street}</td>
      <td>{apartment.street_number}</td>
      <td>{apartment.city}</td>
      <td>{apartment.rent}</td>
      <td>{apartment.latitude}</td>
      <td>{apartment.longitude}</td>
    </tr>
  );
}

export default ApartmentRow;
