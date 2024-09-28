import { useState } from 'react'
import './App.scss'
import ChatBot from './components/ChatBot/ChatBot'
import Header from './components/Header/Header'
import HeaderBar from './components/HeaderBar/HeaderBar'
import Summary from './components/Summary/Summary'
import { Languages } from './enums'
import { SummaryType } from './types'

function App() {

  const [settings, setSettings] = useState({
    language: Languages.polish
  });

  const [responses, setResponses] = useState<SummaryType[]>([]);

  const addResponses = (responseData: SummaryType[])  => setResponses((prev) => [...prev, ...responseData]);

  const changeBotLanguage = (type: Languages) => {
    setSettings((prev) => ({...prev, language: type}));
  }

  console.log(responses);

  return (
    <>
      <HeaderBar />
      <Header settings={settings} changeLanguage={changeBotLanguage} />
      <main className='main-layout'>
        <ChatBot addResponses={addResponses} />
        <Summary settings={settings} responses={responses} />
      </main>
    </>
  )
}

export default App
