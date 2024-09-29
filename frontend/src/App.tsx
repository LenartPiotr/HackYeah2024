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
  const [summaryToggle, setSummaryToggle] = useState<boolean>(false);

  const addResponses = (responseData: SummaryType[]) => {
    const updatedResponses = responseData.map(newResponse => {
      const existingResponseIndex = responses.findIndex(response => response.type === newResponse.type);
      
      if (existingResponseIndex !== -1) {
          return { ...responses[existingResponseIndex], ...newResponse };
      }
      return newResponse;
    });

    setResponses(prevResponses => {
      const allResponses = [...prevResponses];

      updatedResponses.forEach(updatedResponse => {
          const index = allResponses.findIndex(response => response.type === updatedResponse.type);
          if (index !== -1) {
              allResponses[index] = updatedResponse;
          } else {
              allResponses.push(updatedResponse);
          }
      });

      return allResponses;
    });
  }

  const changeBotLanguage = (type: Languages) => {
    setSettings((prev) => ({...prev, language: type}));
  }

  console.log(responses);

  return (
    <>
      <HeaderBar />
      <Header settings={settings} changeLanguage={changeBotLanguage} setSummaryToggle={setSummaryToggle} />
      <main className='main-layout'>
        <ChatBot addResponses={addResponses} />
        <Summary settings={settings} responses={responses} summaryToggle={summaryToggle} />
      </main>
    </>
  )
}

export default App
