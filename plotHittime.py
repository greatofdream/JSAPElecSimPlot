import uproot, argparse
import matplotlib.pyplot as plt

psr = argparse.ArgumentParser()
psr.add_argument('-i', dest="input", help="input  file")
psr.add_argument('-o', dest="output", help="output png file ")
psr.add_argument('-e', dest="eid", help="eid number")
psr.add_argument('-c', dest="ch", nargs='+', help="channel number list")
args = psr.parse_args()
eid = int(args.eid)
chs = [int(i) for i in args.ch]
with uproot.open(args.input) as ipt:
    ht = ipt['SimTriggerInfo']['PEList.HitTime'].array()[eid]
    pet = ipt['SimTriggerInfo']['PEList.PENanoSec'].array()[eid]
    petInw = ipt['SimTriggerInfo']['PEList.HitPosInWindow'].array()[eid]
    chList = ipt['SimTriggerInfo']['PEList.PMTId'].array()[eid]
    print('pet.shape:{};petInw.shape:{}'.format(pet.shape, petInw.shape))
    
    '''
    fig, ax = plt.subplots()
    ax.vlines(pet, 0, 1)
    ax.set_title('PETime in all Channel', size="xx-large", weight="bold")
    ax.set_xlabel('t/ns', size="xx-large", weight="bold")
    ax.set_ylabel('num', size="xx-large", weight="bold")
    ax.set_ylim((0,2))
    ax.set_yticks((0, 1, 2))
    ax.set_yticklabels((0, 1, 2))
    plt.savefig('PETime_eid{}.png'.format(eid))
    plt.close()

    fig, ax = plt.subplots()
    ax.vlines(petInw, 0, 1)
    ax.set_title('PETime in Window in all Channel', size="xx-large", weight="bold")
    ax.set_xlabel('t/ns', size="xx-large", weight="bold")
    ax.set_ylabel('num', size="xx-large", weight="bold")
    ax.set_ylim((0,2))
    ax.set_yticks((0, 1, 2))
    ax.set_yticklabels((0, 1, 2))
    plt.savefig('PETimeInWindow_eid{}.png'.format(eid))
    plt.close()
    for chi in chs:
        fig, ax = plt.subplots()
        ax.vlines(ht[chList==chi], 0, 1)
        ax.set_title('HitTime in Channel{}'.format(chi), size="xx-large", weight="bold")
        ax.set_xlabel('t/ns', size="xx-large", weight="bold")
        ax.set_ylabel('num', size="xx-large", weight="bold")
        ax.set_xlim((0,100))
        ax.set_ylim((0,2))
        ax.set_yticks((0, 1, 2))
        ax.set_yticklabels((0, 1, 2))
        plt.savefig('hitTime_eid{}_ch{}.png'.format(eid, chi))
        plt.close()
        
        fig, ax = plt.subplots()
        ax.vlines(pet[chList==chi], 0, 1)
        ax.set_title('PETime in Channel{}'.format(chi), size="xx-large", weight="bold")
        ax.set_xlabel('t/ns', size="xx-large", weight="bold")
        ax.set_ylabel('num', size="xx-large", weight="bold")
        #ax.set_xlim((0,100))
        ax.set_ylim((0,2))
        ax.set_yticks((0, 1, 2))
        ax.set_yticklabels((0, 1, 2))
        plt.savefig('PETime_eid{}_ch{}.png'.format(eid, chi))
        plt.close()

        fig, ax = plt.subplots()
        ax.vlines(petInw[chList==chi], 0, 1)
        ax.set_title('PETime in Window in Channel{}'.format(chi), size="xx-large", weight="bold")
        ax.set_xlabel('t/ns', size="xx-large", weight="bold")
        ax.set_ylabel('num', size="xx-large", weight="bold")
        # ax.set_xlim((0,100))
        ax.set_ylim((0,2))
        ax.set_yticks((0, 1, 2))
        ax.set_yticklabels((0, 1, 2))
        plt.savefig('PETimeInWindow_eid{}_ch{}.png'.format(eid, chi))
        plt.close()
    '''