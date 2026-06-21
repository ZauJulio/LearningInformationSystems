import React from "react";
import {
  MapContainer,
  Marker,
  Popup,
  TileLayer,
  ZoomControl,
} from "react-leaflet";
import L from "leaflet";

import styles from "../styles/components/Map.module.scss";
import "leaflet/dist/leaflet.css";
import marker from "../public/map-marker.svg";

const mapIcon = L.icon({
  iconUrl: marker,
  iconSize: [58, 68],
  iconAnchor: [29, 68],
  popupAnchor: [0, -60],
});

function Map() {
  return (
    <div>
      <MapContainer
        className={styles.mapContainer}
        center={[-6.4625567, -37.0962424]} // City center
        zoom={14}
      >
        <TileLayer
          attribution='<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
          url="https://api.maptiler.com/maps/basic/{z}/{x}/{y}.png?key=R5r8yv38JwRrZl7m6DHJ"
        />
        <Marker icon={mapIcon} position={[-6.4625567, -37.0962424]}>
          <Popup>Example map marker</Popup>
        </Marker>
      </MapContainer>
      <p>
        <a href="https://www.maptiler.com/copyright/" target="_blank">
          © MapTiler
        </a>{" "}
        <a href="https://www.openstreetmap.org/copyright" target="_blank">
          © OpenStreetMap contributors
        </a>
      </p>
    </div>
  );
}

export default Map;
