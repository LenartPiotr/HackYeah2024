import { useState } from 'react'
import './App.scss'
import ChatBot from './components/ChatBot/ChatBot'
import Header from './components/Header/Header'
import HeaderBar from './components/HeaderBar/HeaderBar'
import Summary from './components/Summary/Summary'
import { Languages } from './enums'

function App() {

  const [settings, setSettings] = useState({
    language: Languages.polish
  });

  const changeBotLanguage = (type: Languages) => {
    setSettings((prev) => ({...prev, language: type}));
  }

  return (
    <>
      <HeaderBar />
      <Header settings={settings} changeLanguage={changeBotLanguage} />
      <main className='main-layout'>
        <ChatBot />
        <Summary settings={settings} />
      </main>
    </>
  )
}

export default App
