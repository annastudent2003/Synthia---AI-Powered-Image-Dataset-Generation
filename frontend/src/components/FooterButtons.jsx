import "./FooterButtons.css";

export default function FooterButtons({ images, prompt }) {
  const handleRegenerate = () => {
    window.location.reload();
  };

  const handleDownloadAll = () => {
    images.forEach((url, index) => {
      const link = document.createElement("a");
      link.href = url;
      link.download = `${prompt.replace(/\s+/g, "_")}_${index + 1}.jpg`;
      link.click();
    });
  };

  return (
    <div className="footer-buttons">
      <button onClick={handleRegenerate}>Regenerate</button>
      <button onClick={handleDownloadAll}>Download All</button>
    </div>
  );
}

