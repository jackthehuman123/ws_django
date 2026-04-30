import { useWebSocket } from "../hooks/useWebSocket";
import MessageList from "./MessageList";

export default function DebugRoom({ roomId }) {
  const { messages, send } = useWebSocket(roomId);

  return (
    <div>
      <p>
        Room: {roomId} - Messages: {messages.length}
      </p>
      <button onClick={() => send("test message from React")}>Send test</button>
      <MessageList messages={messages} />
    </div>
  );
}
