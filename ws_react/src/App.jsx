import { AuthProvider, useAuth } from "./context/AuthContext";
import LoginForm from "./components/LoginForm";

function AppInner() {
  const { user } = useAuth();
  if (!user) return <LoginForm />;
  return <div>Welcome, {user}. (Chat UI goes here)</div>;
}

export default function App() {
  return (
    <AuthProvider>
      <AppInner />
    </AuthProvider>
  )
}
