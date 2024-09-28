import './App.scss'
import ChatBot from './components/ChatBot/ChatBot'
import Header from './components/Header/Header'
import HeaderBar from './components/HeaderBar/HeaderBar'
import Summary from './components/Summary/Summary'

function App() {
  return (
    <>
      <HeaderBar />
      <Header />
      <main className='main-layout'>
        <Summary />
        <ChatBot />
      </main>
    </>
  )
}

export default App
