import "./ImageGrid.css";

export default function ImageGrid({ images }) {
  return (
    <div className="image-grid">
      {images.map((src, index) => (
        <div key={index} className="image-card">
          <img src={src} alt={`Generated ${index}`} />
        </div>
      ))}
    </div>
  );
}
