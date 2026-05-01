export default function RoomSidebar({ rooms, activeRoom, onSelect }) {
  return (
    <div
      style={{ width: "180px", borderRight: "1px solid #ccc", padding: "12px" }}
    >
      <h4 style={{ marginTop: 0 }}>Rooms</h4>
      {rooms.map((room) => (
        <div
          key={room}
          onClick={() => onSelect(room)}
          style={{
            padding: "8px",
            borderRadius: "4px",
            cursor: "pointer",
            background: room === activeRoom ? "#e0e7ff" : "transparent",
            fontWeight: room === activeRoom ? "bold" : "normal",
          }}
        >
          # {room}
        </div>
      ))}
    </div>
  );
}
