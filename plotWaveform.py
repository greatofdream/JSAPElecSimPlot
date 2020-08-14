import uproot, argparse, numpy as np
import matplotlib.pyplot as plt

psr = argparse.ArgumentParser()
psr.add_argument('-i', dest="input", help="input  file")
psr.add_argument('-o', dest="output", help="output png file ")
psr.add_argument('-e', dest="eid", help="eid number")
args = psr.parse_args()
eid = int(args.eid)

fcoincidence = 50
threshold = 967.68

with uproot.open(args.input) as ipt:
    waveformList = ipt['Readout']['Waveform'].array()[eid]
    chList = ipt['Readout']['ChannelId'].array()[eid]
    print('chList.shape:{};waveformList.shape:{}'.format(chList.shape, waveformList.shape))
    waveLength = int(waveformList.shape[0]/chList.shape[0])
    logicAdd = np.zeros((waveLength,))
    for i, chi in enumerate(chList):
        '''
        fig, ax = plt.subplots()
        ax.plot(waveformList[i*waveLength:(i+1)*waveLength])
        ax.set_title('waveform of Channel{}'.format(chi), size="xx-large", weight="bold")
        ax.set_xlabel('t/ns', size="xx-large", weight="bold")
        ax.set_ylabel('adc', size="xx-large", weight="bold")
        plt.savefig('waveform/waveform_eid{}_ch{}.png'.format(eid, chi))
        plt.close()
        
        fig, ax = plt.subplots()
        ax.plot(waveformList[i*waveLength:(i+1)*waveLength])
        ax.set_title('trigger of Channel{}'.format(chi), size="xx-large", weight="bold")
        ax.set_xlabel('t/ns', size="xx-large", weight="bold")
        ax.set_ylabel('adc', size="xx-large", weight="bold")
        plt.savefig('trigger_eid{}_ch{}.png'.format(eid, chi))
        plt.close()
        '''
        logicWave = np.zeros((waveLength,))
        #print(waveformList[i*waveLength:(i+1)*waveLength])
        logicWaveIndex = np.where(np.array(waveformList[i*waveLength:(i+1)*waveLength])<threshold)[0]
        #print(logicWaveIndex)
        if logicWaveIndex.shape[0]==0:
            continue
        cursor = 0
        for cur in logicWaveIndex:
            if cursor>cur:
                continue
            logicWave[cur:(cur+fcoincidence)] = 1
            cursor = cur+fcoincidence
        logicAdd += logicWave
        fig, ax = plt.subplots()
        ax.plot(waveformList[i*waveLength:(i+1)*waveLength])
        ax.axhline(threshold, color='red')
        ax.set_xlim((100,600))
        ax.set_title('trigger of Channel{}'.format(chi), size="xx-large", weight="bold")
        ax.set_xlabel('t/ns', size="xx-large", weight="bold")
        ax.set_ylabel('adc', size="xx-large", weight="bold")
        ax2 = ax.twinx()
        color = 'tab:red'
        ax2.set_ylabel('logic', color=color, size="xx-large", weight="bold")
        ax2.set_ylim((0,2))
        ax2.plot(logicWave,color=color)
        ax2.tick_params(axis='y', labelcolor=color)
        fig.tight_layout()
        plt.savefig('waveform/logic_eid{}_ch{}.png'.format(eid, chi))
        plt.close()
    
    fig, ax = plt.subplots()
    for i, chi in enumerate(chList):
        ax.plot(waveformList[i*waveLength:(i+1)*waveLength], label='ch{}'.format(chi))
        ax.set_title('waveform of all Channel'.format(chi), size="xx-large", weight="bold")
        ax.set_xlabel('t/ns', size="xx-large", weight="bold")
        ax.set_ylabel('adc', size="xx-large", weight="bold")
        #ax.vline(,label='trigger')
        ax2 = ax.twinx()
        color = 'tab:red'
        ax2.set_ylabel('logic', color=color, size="xx-large", weight="bold")
        ax2.plot(logicAdd,color=color)
        ax2.tick_params(axis='y', labelcolor=color)
    ax.axhline(threshold, color='red')
    fig.tight_layout()
    plt.savefig('waveform/logic_eid{}.png'.format(eid))
    plt.close()
    