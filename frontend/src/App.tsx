import { useState } from 'react'
import './App.scss'
import ChatBot from './components/ChatBot/ChatBot'
import Header from './components/Header/Header'
import HeaderBar from './components/HeaderBar/HeaderBar'
import Summary from './components/Summary/Summary'
import { Languages } from './enums'
import { SummaryType, MessageType } from './types'

function App() {

  const [settings, setSettings] = useState({
    language: Languages.polish
  });

  const [responses, setResponses] = useState<SummaryType[]>([]);
  const [summaryToggle, setSummaryToggle] = useState<boolean>(false);
  const [chatData, setChatData] = useState<MessageType[]>([{
    text: messages['welcome-prompt'][settings.language]
  }]);
  const [formName, setFormName] = useState<string|null>(null);

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
    chatData[0].text = messages['welcome-prompt'][type];
  }

  console.log(responses);

  return (
    <>
      <HeaderBar />
      <Header settings={settings} changeLanguage={changeBotLanguage} setSummaryToggle={setSummaryToggle} formName={formName}/>
      <main className='main-layout'>
        <ChatBot addResponses={addResponses} settings={settings} chatData={chatData} setChatData={setChatData} setFormName={setFormName} />
        <Summary settings={settings} responses={responses} summaryToggle={summaryToggle} />
      </main>
    </>
  )
}

const messages = {
  'welcome-prompt': {
      'polish': 'Witaj, opisz mi swoją sytuację abym mógł ci pomóc',
      'english': 'Hello, describe your situation to me so I can help you',
      'ukrainian': 'Привіт, опишіть мені вашу ситуацію, щоб я міг вам допомогти'
  }
}

export default App
